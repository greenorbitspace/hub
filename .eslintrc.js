/* eslint-env node */
module.exports = {
  extends: ['eslint:recommended'],
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
    ecmaVersion: 2021,
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
      files: ['.eslintrc.js', 'tools/**/*.js', 'postcss.config.js'],
      env: { node: true, browser: false },
      globals: {
        module: 'readonly',
        require: 'readonly',
        process: 'readonly',
        __dirname: 'readonly',
      },
      rules: { 'no-undef': 'off' },
    },
    {
      files: [
        'assets/js/prism.js',
        'assets/js/mkdirp-hugo-mod.js',
        'assets/js/plantuml.js',
        'assets/js/markmap.js',
        'assets/js/drawio.js',
      ],
      rules: {
        'no-undef': 'off',
        'no-unused-vars': 'warn',
        'no-empty': 'warn',
        'no-useless-escape': 'warn',
      },
    },
    {
      files: ['static/js/prism.js'],
      rules: {
        'no-undef': 'off',
        'no-prototype-builtins': 'off',
        'no-cond-assign': 'warn',
        'no-useless-escape': 'warn',
        'no-control-regex': 'warn',
        'no-empty': 'warn',
        'no-unused-vars': 'warn',
      },
    },
    {
      files: ['static/js/deflate.js'],
      rules: {
        'no-unused-vars': ['warn', { varsIgnorePattern: '^(deflate|zip_deflate_end)$' }],
        'no-empty': ['warn', { allowEmptyCatch: true }],
      },
    },
  ],
};