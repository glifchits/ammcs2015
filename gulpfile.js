var gulp = require('gulp');
var watch = require('gulp-watch');
var sass = require('gulp-sass');
var imageResize = require('gulp-image-resize');
var rename = require('gulp-rename');
var run = require('gulp-run');
var connect = require('gulp-connect');


gulp.task('images', function() {
  gulp.src('static/images/plenary/*')
    .pipe(imageResize({
      width: 170,
      height: 170,
      upscale: false
    }))
    .pipe(gulp.dest('static/images/plenary/thumbs'));
});

gulp.task('styles', function() {
  gulp.src('static/scss/*.scss')
    .pipe(sass())
    .pipe(gulp.dest('static/css'))
    .pipe(gulp.dest('build/static/css'));
});

gulp.task('freeze', function() {
  run('python ./freezer.py').exec();
});

gulp.task('serve', function() {
  connect.server({
    root: 'build',
    livereload: true,
    port: 5000
  });
});

gulp.task('default', ['styles', 'images', 'freeze', 'serve'], function() {
  gulp.watch('static/scss/*.scss', function(evt) {
    gulp.run('styles');
  });
  gulp.watch(['**/*.py', 'pages/**/*.html'], function() {
    gulp.run('freeze');
  });
});
