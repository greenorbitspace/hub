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
    WorkerGlobalScope: 'readonly', // Web Worker global scope
    deflate: 'readonly',            // Used in deflate.js
    zip_deflate_end: 'readonly',   // Used in deflate.js
    global: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module',
  },
  rules: {
    'no-unused-vars': ['error', { argsIgnorePattern: '^_' }], // Ignore unused vars starting with _
    'no-undef': 'error',
    'no-empty': 'warn',
    'no-prototype-builtins': 'off', // Allow direct hasOwnProperty calls to suppress those warnings
    'no-cond-assign': ['error', 'except-parens'],
    'no-useless-escape': 'warn',
  },
  overrides: [
    {
      // Node config files override
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
        'no-undef': 'off',
      },
    },
    {
      // Third-party legacy scripts with common ESLint issues
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
      // Deflate.js specific overrides to address unused vars & empty blocks
      files: ['static/js/deflate.js'],
      rules: {
        'no-unused-vars': ['warn', { varsIgnorePattern: '^(deflate|zip_deflate_end)$' }],
        'no-empty': ['warn', { allowEmptyCatch: true }],
      },
    },
  ],
};