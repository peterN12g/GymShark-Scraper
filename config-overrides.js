const { override, addWebpackDevServer } = require('customize-cra');

module.exports = override(
  addWebpackDevServer(config => {
    return {
      ...config,
      proxy: {
        '/api': {
          target: 'http://localhost:8080',
          secure: false,
        },
      },
    };
  })
);
