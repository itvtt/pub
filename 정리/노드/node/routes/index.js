const express=require("express");
const app = express.Router();
const postRouter = require("./post");
const categoryRouter = require("./category");



app.use("/", (req, res) => {
    console.log(("index"));
    });

module.exports = router;
