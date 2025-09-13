const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

class ConfigLoader {
  constructor(options = {}) {
    this.configPaths = options.configPaths || ['config.yaml', 'config.yml', 'config.json'];
    this.envPrefix = options.envPrefix || 'TROJAN_';
    this.config = {};
  }

  /**
   * Load configuration from files and environment variables
   * Priority: Environment variables > Config file > Default values
   */
  load() {
    // Load from config file
    this.loadFromFile();
    
    // Override with environment variables
    this.loadFromEnvironment();
    
    return this.config;
  }

  /**
   * Load configuration from the first available config file
   */
  loadFromFile() {
    for (const configPath of this.configPaths) {
      const fullPath = path.resolve(configPath);
      
      if (fs.existsSync(fullPath)) {
        try {
          const content = fs.readFileSync(fullPath, 'utf8');
          
          if (configPath.endsWith('.json')) {
            this.config = JSON.parse(content);
          } else if (configPath.endsWith('.yaml') || configPath.endsWith('.yml')) {
            this.config = yaml.load(content);
          }
          
          console.log(`Configuration loaded from: ${configPath}`);
          return;
        } catch (error) {
          console.warn(`Failed to load config from ${configPath}: ${error.message}`);
        }
      }
    }
    
    console.log('No config file found, using default/environment configuration');
  }

  /**
   * Load and override configuration from environment variables
   * Supports nested configuration using double underscore separator
   * Example: TROJAN_DATABASE__HOST=localhost -> config.database.host = "localhost"
   */
  loadFromEnvironment() {
    const envVars = Object.keys(process.env)
      .filter(key => key.startsWith(this.envPrefix))
      .reduce((vars, key) => {
        const configKey = key.slice(this.envPrefix.length);
        vars[configKey] = process.env[key];
        return vars;
      }, {});

    // Apply environment variables to config
    Object.keys(envVars).forEach(key => {
      const value = this.parseValue(envVars[key]);
      this.setNestedValue(this.config, key, value);
    });

    if (Object.keys(envVars).length > 0) {
      console.log(`Applied ${Object.keys(envVars).length} environment variable overrides`);
    }
  }

  /**
   * Parse string values to appropriate types
   */
  parseValue(value) {
    // Try to parse as number
    if (/^\d+$/.test(value)) {
      return parseInt(value, 10);
    }
    
    if (/^\d*\.\d+$/.test(value)) {
      return parseFloat(value);
    }

    // Try to parse as boolean
    if (value.toLowerCase() === 'true') return true;
    if (value.toLowerCase() === 'false') return false;

    // Try to parse as JSON
    if ((value.startsWith('{') && value.endsWith('}')) || 
        (value.startsWith('[') && value.endsWith(']'))) {
      try {
        return JSON.parse(value);
      } catch {
        // If JSON parsing fails, return as string
      }
    }

    return value;
  }

  /**
   * Set nested object values using double underscore notation
   * Example: "DATABASE__HOST" -> config.database.host
   */
  setNestedValue(obj, path, value) {
    const keys = path.split('__').map(key => key.toLowerCase());
    let current = obj;

    for (let i = 0; i < keys.length - 1; i++) {
      const key = keys[i];
      if (!(key in current) || typeof current[key] !== 'object') {
        current[key] = {};
      }
      current = current[key];
    }

    current[keys[keys.length - 1]] = value;
  }

  /**
   * Get configuration value by path
   */
  get(path, defaultValue = undefined) {
    const keys = path.split('.');
    let current = this.config;

    for (const key of keys) {
      if (current && typeof current === 'object' && key in current) {
        current = current[key];
      } else {
        return defaultValue;
      }
    }

    return current;
  }

  /**
   * Get all configuration
   */
  getAll() {
    return { ...this.config };
  }
}

module.exports = ConfigLoader;