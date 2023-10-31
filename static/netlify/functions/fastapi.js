const { spawnSync } = require('child_process');

exports.handler = async (event, context) => {
  const result = spawnSync('python', ['main.py'], { encoding: 'utf-8' });
  return {
    statusCode: 200,
    body: result.stdout,
  };
};
