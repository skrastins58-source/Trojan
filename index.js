#!/usr/bin/env node

const ConfigLoader = require('./config');

function main() {
  console.log('=== Trojan Configuration Demo ===\n');

  // Initialize configuration loader
  const configLoader = new ConfigLoader({
    configPaths: ['config.yaml', 'config.yml', 'config.json'],
    envPrefix: 'TROJAN_'
  });

  // Load configuration
  const config = configLoader.load();

  console.log('\n=== Current Configuration ===');
  console.log(JSON.stringify(config, null, 2));

  // Demonstrate accessing configuration values
  console.log('\n=== Configuration Access Examples ===');
  console.log(`App Name: ${configLoader.get('app.name', 'Unknown App')}`);
  console.log(`App Port: ${configLoader.get('app.port', 8080)}`);
  console.log(`Database Host: ${configLoader.get('database.host', 'localhost')}`);
  console.log(`Database Port: ${configLoader.get('database.port', 5432)}`);
  console.log(`Debug Mode: ${configLoader.get('app.debug', false)}`);
  console.log(`Caching Enabled: ${configLoader.get('features.enable_caching', false)}`);

  // Example of accessing nested configuration
  const dbConfig = configLoader.get('database');
  if (dbConfig) {
    console.log('\n=== Database Configuration ===');
    console.log(`Full Database Config:`, dbConfig);
  }

  // Example of accessing non-existent configuration with defaults
  console.log('\n=== Default Value Examples ===');
  console.log(`Non-existent key: ${configLoader.get('non.existent.key', 'default-value')}`);
  console.log(`Missing feature flag: ${configLoader.get('features.non_existent_flag', false)}`);

  console.log('\n=== Environment Variables Demo ===');
  console.log('Try running with environment variables to see overrides:');
  console.log('Example: TROJAN_APP__PORT=8080 TROJAN_DATABASE__HOST=production-db node index.js');
  console.log('Example: TROJAN_APP__DEBUG=false TROJAN_FEATURES__ENABLE_CACHING=false node index.js');

  // Simulate starting the application
  const port = configLoader.get('app.port', 3000);
  const appName = configLoader.get('app.name', 'Trojan App');
  
  console.log(`\n=== Starting ${appName} ===`);
  console.log(`Server would start on port: ${port}`);
  console.log(`Environment: ${configLoader.get('app.environment', 'production')}`);
  console.log(`Debug mode: ${configLoader.get('app.debug', false) ? 'enabled' : 'disabled'}`);
}

if (require.main === module) {
  main();
}

module.exports = { main };