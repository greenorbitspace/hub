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
    WorkerGlobalScope: 'readonly',  // Web Worker global scope
    deflate: 'readonly',             // Used in deflate.js
    zip_deflate_end: 'readonly',    // Used in deflate.js
    global: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2021,
    sourceType: 'module',
  },
  rules: {
    // Allow unused function arguments if prefixed with underscore
    'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    'no-undef': 'error',
    'no-empty': 'warn',               // Warn on empty blocks, allow empty catch (overridden below)
    'no-prototype-builtins': 'off',  // Allow direct calls like obj.hasOwnProperty()
    'no-cond-assign': ['error', 'except-parens'],
    'no-useless-escape': 'warn',
  },
  overrides: [
    {
      // Node.js config and tool scripts
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
        // Allow Node globals without 'no-undef' errors
        'no-undef': 'off',
      },
    },
    {
      // Legacy or third-party front-end scripts with known ESLint exceptions
      files: [
        'assets/js/prism.js',
        'assets/js/mkdirp-hugo-mod.js',
        'assets/js/plantuml.js',
        'assets/js/markmap.js',
        'assets/js/drawio.js',
      ],
      rules: {
        'no-undef': 'off',        // Allow undefined globals typical in legacy scripts
        'no-unused-vars': 'warn', // Warn on unused vars instead of error
        'no-empty': 'warn',       // Warn on empty blocks
        'no-useless-escape': 'warn',
      },
    },
    {
      // deflate.js requires special handling due to unused vars and empty catch blocks
      files: ['static/js/deflate.js'],
      rules: {
        'no-unused-vars': ['warn', { varsIgnorePattern: '^(deflate|zip_deflate_end)$' }],
        'no-empty': ['warn', { allowEmptyCatch: true }],
      },
    },
  ],
};