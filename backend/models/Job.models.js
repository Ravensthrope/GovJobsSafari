import mongoose from "mongoose";

const jobSchema = new mongoose.Schema({
  postDate: {
    type: String,
    required: true,
  },
  organisation: {
    type: String,
    required: true,
  },
  postName: {
    type: String,
    required: true,
  },
  qualification: {
    type: String,
    required: true,
  },
  lastDate: {
    type: String,
    required: true,
  },
  category: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Category",
    required: true,
  },
});

const Job = mongoose.model("Job", jobSchema);
module.exports = Job;
