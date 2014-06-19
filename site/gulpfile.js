var gulp = require('gulp'),
	watch = require('gulp-watch'),
	sass = require('gulp-sass');

gulp.task('styles', function() {
	gulp.src('static/scss/*.scss')
		.pipe(sass())
		.pipe(gulp.dest('static/css'));
});

gulp.task('default', ['styles'], function() {
	gulp.watch('static/scss/*.scss', function(evt) {
		gulp.run('styles');
	});
});
