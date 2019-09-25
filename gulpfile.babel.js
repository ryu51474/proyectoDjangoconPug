const gulp = require('gulp') ;
const pug = require('gulp-pug')
const browserSync = require('browser-sync')
const plumber = require('gulp-plumber')

const servidor = browserSync.create()

gulp.task('pug',()=>{
    return gulp.src('./Proyecto1/pug/*.pug')
                .pipe(plumber())
                .pipe(pug({
                    pretty:true
                }))
                .pipe(gulp.dest('./Proyecto1/plantillas/'))
})


gulp.task('default',()=>{
    servidor.init({
        server: './Proyecto1/plantillas'
    })
    gulp.watch('./Proyecto1/pug/*.pug', gulp.series('pug')).on('change', servidor.reload)
})