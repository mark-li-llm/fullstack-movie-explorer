module.exports = {
  extends: ['airbnb', 'airbnb/hooks'],
  env: {
    browser: true,
    node: true,
    es2021: true,
    jest: true,
  },
  parserOptions: {
    ecmaVersion: 2022,
    sourceType: 'module',
  },
  rules: {
    'react/jsx-filename-extension': 0,
    'react/no-array-index-key': 0,
    'react-hooks/exhaustive-deps': 0,
    'react/react-in-jsx-scope': 0, // React 17+ new JSX transform
    'arrow-parens': 0,
    'object-curly-newline': 0,
    'no-alert': 'off',
    'no-console': 0,
    'comma-dangle': ['error', 'always-multiline'],
    'implicit-arrow-linebreak': 'off',
    'no-confusing-arrow': 'off',
    'function-paren-newline': 'off',
  },
};
