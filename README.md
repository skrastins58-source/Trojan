# Trojan

A configurable Node.js application demonstrating configuration management via config files and environment variables.

## Features

- **Multiple Configuration Formats**: Supports both YAML and JSON configuration files
- **Environment Variable Overrides**: Environment variables take precedence over config file values
- **Nested Configuration**: Support for nested configuration with dot notation access
- **Type Conversion**: Automatic type conversion for environment variables (strings, numbers, booleans, JSON)
- **Default Values**: Graceful fallback to default values when configuration is missing
- **Priority System**: Environment variables > Config file > Default values

## Quick Start

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Run the application:**
   ```bash
   npm start
   ```
   or
   ```bash
   node index.js
   ```

## Configuration

### Configuration Files

The application searches for configuration files in the following order:
1. `config.yaml`
2. `config.yml`
3. `config.json`

The first file found will be used as the base configuration.

#### Sample YAML Configuration (`config.yaml`)

```yaml
# Application settings
app:
  name: "Trojan Application"
  version: "1.0.0"
  environment: "development"
  debug: true
  port: 3000

# Database configuration
database:
  host: "localhost"
  port: 5432
  name: "trojan_db"
  username: "trojan_user"
  password: "default_password"
  ssl: false
  pool:
    min: 2
    max: 10
    idle_timeout: 30000

# Logging configuration
logging:
  level: "info"
  file: "./logs/app.log"
  max_size: "10MB"
  max_files: 5

# External services
services:
  redis:
    host: "localhost"
    port: 6379
    password: null
  
  api:
    base_url: "https://api.example.com"
    timeout: 5000
    retry_attempts: 3

# Feature flags
features:
  enable_caching: true
  enable_metrics: false
  enable_auth: true
```

#### Sample JSON Configuration (`config.json`)

```json
{
  "app": {
    "name": "Trojan Application",
    "version": "1.0.0",
    "environment": "development",
    "debug": true,
    "port": 3000
  },
  "database": {
    "host": "localhost",
    "port": 5432,
    "name": "trojan_db",
    "username": "trojan_user",
    "password": "default_password",
    "ssl": false,
    "pool": {
      "min": 2,
      "max": 10,
      "idle_timeout": 30000
    }
  },
  "logging": {
    "level": "info",
    "file": "./logs/app.log",
    "max_size": "10MB",
    "max_files": 5
  },
  "services": {
    "redis": {
      "host": "localhost",
      "port": 6379,
      "password": null
    },
    "api": {
      "base_url": "https://api.example.com",
      "timeout": 5000,
      "retry_attempts": 3
    }
  },
  "features": {
    "enable_caching": true,
    "enable_metrics": false,
    "enable_auth": true
  }
}
```

### Environment Variables

Environment variables can override any configuration value. Use the prefix `TROJAN_` followed by the configuration path with double underscores (`__`) separating nested levels.

#### Environment Variable Examples

```bash
# Override app port
export TROJAN_APP__PORT=8080

# Override database host
export TROJAN_DATABASE__HOST=production-db

# Override debug mode
export TROJAN_APP__DEBUG=false

# Override nested database pool settings
export TROJAN_DATABASE__POOL__MAX=20

# Override feature flags
export TROJAN_FEATURES__ENABLE_CACHING=false

# Multiple overrides
export TROJAN_APP__PORT=9000
export TROJAN_APP__ENVIRONMENT=production
export TROJAN_DATABASE__HOST=prod-db.example.com
export TROJAN_DATABASE__PORT=5433
```

#### Running with Environment Variables

```bash
# Single command with environment variables
TROJAN_APP__PORT=8080 TROJAN_DATABASE__HOST=production-db node index.js

# Or set them first
export TROJAN_APP__PORT=8080
export TROJAN_DATABASE__HOST=production-db
export TROJAN_APP__DEBUG=false
npm start
```

### Configuration Access

The configuration system provides a simple API for accessing configuration values:

```javascript
const ConfigLoader = require('./config');

// Initialize configuration loader
const configLoader = new ConfigLoader({
  configPaths: ['config.yaml', 'config.yml', 'config.json'],
  envPrefix: 'TROJAN_'
});

// Load configuration
const config = configLoader.load();

// Access configuration values with dot notation
const appName = configLoader.get('app.name', 'Default App Name');
const dbHost = configLoader.get('database.host', 'localhost');
const debugMode = configLoader.get('app.debug', false);

// Get entire configuration sections
const databaseConfig = configLoader.get('database');

// Get all configuration
const allConfig = configLoader.getAll();
```

## Type Conversion

Environment variables are automatically converted to appropriate types:

- **Numbers**: `"123"` → `123`, `"12.34"` → `12.34`
- **Booleans**: `"true"` → `true`, `"false"` → `false`
- **JSON**: `'{"key":"value"}'` → `{key: "value"}`, `'[1,2,3]'` → `[1,2,3]`
- **Strings**: Everything else remains as string

## Priority System

Configuration values are resolved in the following priority order:

1. **Environment Variables** (highest priority)
2. **Configuration File** (config.yaml, config.yml, or config.json)
3. **Default Values** (provided in code, lowest priority)

## Examples

### Basic Usage

```bash
# Use default config file
node index.js

# Override specific values
TROJAN_APP__PORT=8080 node index.js

# Production configuration
TROJAN_APP__ENVIRONMENT=production \
TROJAN_APP__DEBUG=false \
TROJAN_DATABASE__HOST=prod-db.company.com \
TROJAN_DATABASE__PORT=5433 \
node index.js
```

### Docker Environment

```dockerfile
# Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Set production environment variables
ENV TROJAN_APP__ENVIRONMENT=production
ENV TROJAN_APP__DEBUG=false
ENV TROJAN_APP__PORT=3000

CMD ["npm", "start"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  trojan:
    build: .
    ports:
      - "3000:3000"
    environment:
      - TROJAN_APP__PORT=3000
      - TROJAN_DATABASE__HOST=postgres
      - TROJAN_DATABASE__PORT=5432
      - TROJAN_DATABASE__PASSWORD=secret
  
  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=trojan_db
      - POSTGRES_USER=trojan_user
      - POSTGRES_PASSWORD=secret
```

## Development

### Project Structure

```
.
├── index.js              # Main application entry point
├── config.js             # Configuration loader module
├── config.yaml           # YAML configuration file
├── config.json           # JSON configuration file
├── package.json          # Node.js project configuration
├── .gitignore            # Git ignore rules
└── README.md             # This documentation
```

### Testing Configuration

Test different configuration scenarios:

```bash
# Test with YAML config (default)
node index.js

# Test with JSON config (rename YAML file temporarily)
mv config.yaml config.yaml.bak
node index.js
mv config.yaml.bak config.yaml

# Test with environment variables only
mv config.yaml config.yaml.bak
mv config.json config.json.bak
TROJAN_APP__NAME="Env Only" TROJAN_APP__PORT=9000 node index.js
mv config.yaml.bak config.yaml
mv config.json.bak config.json

# Test complex environment variable overrides
TROJAN_APP__PORT=8080 \
TROJAN_DATABASE__HOST=test-db \
TROJAN_DATABASE__POOL__MAX=50 \
TROJAN_FEATURES__ENABLE_CACHING=false \
node index.js
```

## Configuration Best Practices

1. **Use config files for default/development settings**
2. **Use environment variables for deployment-specific overrides**
3. **Keep sensitive data (passwords, API keys) in environment variables only**
4. **Document all configuration options and their defaults**
5. **Use meaningful prefixes for environment variables**
6. **Validate critical configuration values at startup**

## Dependencies

- [js-yaml](https://www.npmjs.com/package/js-yaml): YAML parsing support

## License

ISC