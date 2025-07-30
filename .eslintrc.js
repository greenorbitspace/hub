module.exports = {
  env: {
    browser: true,
    node: true,
    es2021: true,
  },
  globals: {
    jQuery: 'readonly',
    bootstrap: 'readonly',
    lunr: 'readonly',
    WorkerGlobalScope: 'readonly',
    deflate: 'readonly',
    zip_deflate_end: 'readonly',
    global: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
  },
  rules: {
    'no-unused-vars': ['error', { argsIgnorePattern: '^_' }], // Allow unused vars starting with _
    'no-undef': 'error',
    'no-empty': 'warn',
    'no-prototype-builtins': 'off', // Disable to allow Object.prototype.hasOwnProperty calls
    'no-cond-assign': ['error', 'except-parens'], // Allow assignments inside parentheses
    'no-useless-escape': 'warn', // Warn on unnecessary escapes
  },
  overrides: [
    {
      // Node-specific config files (ESLint config, tooling, postcss)
      files: ['.eslintrc.js', 'tools/**/*.js', 'postcss.config.js'],
      env: {
        node: true,
        browser: false,
      },
      globals: {
        module: 'readonly',
        require: 'readonly',
        process: 'readonly',
        __dirname: 'readonly',
      },
      rules: {
        'no-undef': 'off', // Node globals allowed, ignore no-undef here
      },
    },
    {
      // Legacy or third-party scripts with known issues
      files: [
        'assets/js/prism.js',
        'assets/js/mkdirp-hugo-mod.js',
        'assets/js/plantuml.js',
        'assets/js/markmap.js',
        'assets/js/drawio.js',
      ],
      rules: {
        'no-undef': 'off',      // Suppress undefined global errors
        'no-unused-vars': 'warn', 
        'no-empty': 'warn',
        'no-useless-escape': 'warn',
      },
    },
  ],
};