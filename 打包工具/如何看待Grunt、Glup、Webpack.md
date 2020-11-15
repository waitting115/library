## 如何看待 Grunt、Gulp 和 Webpack

相信小伙伴们不仅听说过 Gulp 和 webpack ，还听说过 Grunnt。一般都觉得他们都是打包工具，但其实还是有区别的 。更准确的讲，**Grunt和Gulp属于任务流工具`Tast Runner` , 而 webpack属于模块打包工具 `Bundler`。**

![img](https:////upload-images.jianshu.io/upload_images/8646214-2a3bdb51c88dce6e.png?imageMogr2/auto-orient/strip|imageView2/2/w/1166/format/webp)

打包工具的发展史



## # Tast Runner（任务流工具）

### | Grunt

  **Grunt的出现早于Gulp**，Gulp是后起之秀。他们的本质都是通过 JavaScript 语法实现了shell script 命令的一些功能。比如利用`jshint`插件 实现 JavaScript 代码格式检查这一个功能。早期需要手动在命令行中输入 **`jshint test.js`**，而 Grunt 则通过文件 Gruntfile.js 进行配置



```jsx
// Gruntfile.js
module.exports = function(grunt) {
  grunt.initConfig({
    // js格式检查任务
    jshint: {
      src: 'src/test.js'
    }
    //  代码压缩打包任务
    uglify: {}
  });
  // 导入任务插件
  grunt.loadnpmTasks('grunt-contrib-uglify');
  // 注册自定义任务, 如果有多个任务可以添加到数组中
  grunt.regusterTask('default', ['jshint'])
}
```

 

### | Gulp

  **Gulp吸取了Grunt的优点，拥有更简便的写法**，通过流（`Stream`）的概念来简化多任务之间的配置和输出，让任务更加简洁和容易上手。通过配置gulpfile.js文件来实现，一个简单的gulpfile.js配置如下



```jsx
// gulpfile.js
var gulp = require('gulp');
var jshint = require('gulp-jshint');
var uglify = require('gulp-uglify');

// 代码检查任务 gulp 采取了pipe 方法，用流的方法直接往下传递
gulp.task('lint', function() {
  return gulp.src('src/test.js')
    .pipe(jshint())
    .pipe(jshint.reporter('default'));
});

// 压缩代码任务
gulp.task('compress'， function() {
  return gulp.src('src/test.js')
    .pipe(uglify())
    .pipe(gulp.dest('build'));
});

// 将代码检查和压缩组合，新建一个任务
gulp.task('default', ['lint', 'compress']);
```

  你会觉得，规则和结构上都太像了。没问题，gulp本身就是借鉴了grunt的经验进行升级和加入一些新特性。正因为流管理多任务配置输出方式的提高，人们逐渐选择使用Gulp而放弃grunt。

## # Bundler（模块打包工具）

### | browserify

  browserify 是早期的模块打包工具，是**先驱者**，踏实的浏览器端使用CommonJS规范（`require--module.export`）的格式组织代码成为可能。在这之前，因为CommonJS与浏览器特性的不兼容问题，更多使用的是AMD（`defined--require`）规范，当然后来又发展了ES6模块规范（`require--export`）

  假设有如下模块add.js 和 文件test.js，test.js 使用CommonJS规范导入了模块add.js



```jsx
// add.js
module.exports = function(a, b) {
  return a + b
};

// test.js
var add = require('./add.js');
console.log(add(1, 2));  // 3
```

  我们知道，如果直接执行是执行不成功的，因为浏览器无法识别CommonJS语法，而browserify就是用来处理这个问题的，他将CommonJS语法进行装换，在命令行执行功如下



```css
browserify test.js > bundle.js
```

  生成的bundle.js就是已经处理完毕，可供浏览器执行使用的文件，只需要将它插入到``中即可。

### | webpack

  webpack是后起之秀，它支持了AMD 和 CommonJS 类型，通过`loader` 机制也可以使用ES6模块格式。还有强大的 `code splitting`。webpack 是个十分强大的工具，它正在向一个全能型的构建工具发展。

  webpack通过配置文件 webpack.config.js 进行功能配置，一个配置案例如下



```jsx
'use strict'
const path = require('path')
const webpack = require('webpack')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const merge = require('webpack-merge')
const utils = require('./utils')

var config = {
  // 入口
  entry: {
    app: './src/main.js'
  },
  // 出口
  output: {
    path: config.build.assetsRoot,
    filename: '[name].js',
    publicPath: process.env.NODE_ENV === 'production'
      ? config.build.assetsPublicPath
      : config.dev.assetsPublicPath
  },
  // 加载器配置（需要加载器转化的模块类型）
  module: {
    rules: [
      {
        test: '/\.css$/',
        use: [ 'style-loader', 'css-loader' ]
      }
    ]
  }
  // 插件
  plugins: [
    new webpack.DefinePlugin({
      'process.env': require('../config/dev.env')
    }),
    new webpack.HotModuleReplacementPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'index.html',
      inject: true
    }),
  ]

}

module.exports = config
```

  **一个相比比较全面的配置主要包含五个部分： 入口，出口，加载器，插件，模式。分别指定了开始读取文件的位置，编译后输出文件的路径，ES6语法转化加载器，更复杂功能的插件以及指定执行的环境变量。**
 

## # 区别

   相信大家看完上文后对于他们的区别也心中有数

  **gulp和grunt是流管理工具**，通过一个个task配置执行用户需要的功能，如格式检验，代码压缩等，值得一提的是，经过这两者处理的代码只是局部变量名被替换简化，**整体并没有发生改变，还是你的代码。**

  而webpack则进行了更彻底的打包处理，更加偏向对模块语法规则进行转换。主要任务是**突破浏览器的鸿沟，将原本浏览器不能识别的规范和各种各样的静态文件进行分析，压缩，合并，打包，最后生成浏览器支持的代码**，因此，**webapck打包过后的代码已经不是你写的代码了**，或许你再去看，已经看不懂啦