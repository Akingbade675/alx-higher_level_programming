#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const tasks = {};

    for (const task of data) {
      if (!tasks[task.userId]) {
        const compls = data.filter(n => {
          if (n.userId === task.userId && n.completed) { return true; }
          return false;
        });
        if (compls.length) tasks[task.userId] = compls.length;
      }
    }

    console.log(tasks);
  }
});
