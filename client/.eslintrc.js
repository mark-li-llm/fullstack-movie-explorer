module.exports = {
  extends: ['airbnb', 'airbnb/hooks'],
  rules: {
    'react/jsx-filename-extension': 0,
    'react/no-array-index-key': 0,
    'react-hooks/exhaustive-deps': 0,
    'no-alert': 'off', // 允许 alert（如果你不想用 alert，可以去掉这行）
    'comma-dangle': ['error', 'always-multiline'],
    'implicit-arrow-linebreak': 'off',
    'no-confusing-arrow': 'off',
    'function-paren-newline': 'off',
  },
  env: {
    browser: true,
    node: true,
  },
};
