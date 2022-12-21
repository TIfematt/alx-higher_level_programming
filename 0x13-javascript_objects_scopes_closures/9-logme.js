#!/usr/bin/node
let tmp = 0;

exports.logMe = function (item) {
  console.log(tmp + ': ' + item);
  tmp++;
};

logMe('Hello');
logMe('Best');
logMe('School');
