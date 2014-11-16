var gulp = require('gulp'),
	watch = require('gulp-watch'),
	sass = require('gulp-sass'),
	imageResize = require('gulp-image-resize'),
	rename = require('gulp-rename');


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
		.pipe(gulp.dest('static/css'));
});

gulp.task('default', ['styles', 'images'], function() {
	gulp.watch('static/scss/*.scss', function(evt) {
		gulp.run('styles');
	});
});
