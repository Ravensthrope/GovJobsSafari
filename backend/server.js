import Express from "express";
import dotenv from "dotenv";
import mongoose, { mongo } from "mongoose";
import cors from "cors";
import { fileURLToPath } from "url";
import { dirname } from "path";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = Express();
dotenv.config({ path: `${__dirname}/../.env` });
mongoose.connect(process.env.MONGO_URL);

app.use(cors());
app.use(Express.json());

const port = process.env.PORT;
app.listen(port, () => {
  console.log(`App is listening on port: ${port}`);
});
