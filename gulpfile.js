var gulp = require('gulp'),
sass = require('gulp-sass'),
concat = require('gulp-concat');

// SASS TASK & VARIABLES
var sassInput = "./build-app/sass/**/*.scss",
sassOutput = "./src/css",
sassOptions = {
  errToConsole: true,
  outputStyle: 'expanded'
};

gulp.task('buildSass', function(){
  return gulp
    .src(sassInput)
    .pipe(sass(sassOptions)).on('error', sass.logError)
    .pipe(gulp.dest(sassOutput));
});

// JS TASKS & VARIABLES
var jsInput = "./build-app/js/**/*.js",
jsOutput = "./src/js";

gulp.task('buildJs', function(){
  return gulp
    .src(jsInput)
    .pipe(concat('app.js'))
    .pipe(gulp.dest(jsOutput));
});

gulp.task('watch', function () {
  gulp.watch(sassInput, ['buildSass'])
    .on('change', function (event) {
      console.log('File:' + event.path + ' was ' + event.type + ' running task...');
    });
  gulp.watch(jsInput, ['buildJs'])
    .on('change', function (event) {
      console.log('File:' + event.path + ' was ' + event.type + ' running task...');
    });
});

gulp.task('default', ['watch', 'buildSass', 'buildJs']);