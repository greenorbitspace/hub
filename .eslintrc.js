module.exports = {
  env: {
    browser: true,     // for browser globals like window, document, jQuery
    node: true,        // for Node.js globals like module, require, process, __dirname
    es2021: true
  },
  globals: {
    jQuery: 'readonly',
    bootstrap: 'readonly',
    lunr: 'readonly',
    WorkerGlobalScope: 'readonly',
    deflate: 'readonly',
    zip_deflate_end: 'readonly',
    global: 'readonly'
  },
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module'
  },
  rules: {
    'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    'no-undef': 'error',
    'no-empty': 'warn',
    'no-prototype-builtins': 'off',
    'no-cond-assign': ['error', 'except-parens'],
    'no-useless-escape': 'warn'
  }
};