module.exports = function(grunt) {

	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		sass: {
			dist: {
				files: {
					'static/css/styles.css': 'static/scss/styles.scss',
					'static/css/side-menu.css': 'static/scss/side-menu.scss',
					'static/css/side-menu-old-ie.css': 'static/scss/side-menu-old-ie.scss'
				}
			}
		},
		watch: {
			css: {
				files: '**/*.scss',
				tasks: ['sass']
			}
		}
	});
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.registerTask('default', ['watch']);
};
