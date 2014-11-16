var gulp = require('gulp'),
	watch = require('gulp-watch'),
	sass = require('gulp-sass'),
	imageResize = require('gulp-image-resize'),
	rename = require('gulp-rename'),
	run = require('gulp-run'),
	connect = require('gulp-connect');


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
