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
    'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    'no-undef': 'error',
    'no-empty': 'warn',
    'no-prototype-builtins': 'off',
    'no-cond-assign': ['error', 'except-parens'],
    'no-useless-escape': 'warn',
  },
  overrides: [
    {
      files: ['.eslintrc.js', 'tools/**/*.js'],  // Add any Node-only config/tooling files here
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
        'no-undef': 'off',  // Allow module, require, etc in config files
      },
    },
  ],
};