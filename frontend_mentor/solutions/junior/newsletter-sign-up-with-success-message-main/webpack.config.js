const path = require("path")
const HtmlWebpackPlugin = require("html-webpack-plugin")

module.exports = {
  mode: "development",
  context: path.resolve(__dirname, "src"),
  entry: {
    main: "./main.js",
  },
  output: {
    filename: "[name].[contenthash].js",
    path: path.resolve(__dirname, "dist"),
    clean: true,
    publicPath: '/',
  },
  devtool: "inline-source-map",
  // devServer: {
  //   static: path.resolve(__dirname, "dist"),
  // },
  optimization: {
    runtimeChunk: "single",
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "./index.html",
      favicon: "./assets/images/favicon-32x32.png",
    }),

  ],
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif|img)$/i,
        type: "asset/resource",
      },
      {
        test: /\.html$/i,
        loader: "html-loader",
      },
    ],
  },
}
