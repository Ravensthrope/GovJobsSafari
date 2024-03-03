import Express from "express";
import dotenv from "dotenv";

dotenv.config();
console.log("Environment variables: ", process.env);
const app = Express();

app.get("/", (req, res) => {
  res.send("Hi");
});

const port = process.env.PORT;
app.listen(port, () => {
  console.log(`App is listening on port: ${port}`);
});
