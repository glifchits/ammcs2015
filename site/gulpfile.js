var gulp = require('gulp'),
	watch = require('gulp-watch'),
	sass = require('gulp-sass');

gulp.task('default', function() {
	gulp.src('static/scss/*.scss')
		.pipe(watch(function(files) {
			return files.pipe(sass())
				.pipe(gulp.dest('static/css'));
		}));
});
