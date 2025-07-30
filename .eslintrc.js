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
      files: ['.eslintrc.js', 'tools/**/*.js', 'postcss.config.js'], // added postcss config
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
      files: ['assets/js/prism.js', 'assets/js/mkdirp-hugo-mod.js', 'assets/js/plantuml.js', 'assets/js/markmap.js', 'assets/js/drawio.js'], // known legacy or third-party scripts
      rules: {
        'no-undef': 'off',      // suppress undefined globals for legacy scripts
        'no-unused-vars': 'warn', 
        'no-empty': 'warn',
        'no-useless-escape': 'warn',
      },
    },
  ],
};