import { useState } from "react";

function FileUpload() {
  const [uploadedFiles, setUploadedFiles] = useState<File[]>([]);

  function handleFileChange(e: React.ChangeEvent<HTMLInputElement>) {
    if (e.target.files) {
      setUploadedFiles(Array.from(e.target.files));
    }
  }

  async function handleUpload(e: React.FormEvent) {
    e.preventDefault();

    for (const file of uploadedFiles) {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch("http://localhost:8000/ingest_file", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      console.log("How'd it go?: ", data.message);
    }
  }

  return (
    <div className="card">
      <div className="card-heading">
        <span className="card-heading-icon">📁</span>
        Upload Documents
      </div>
      <form onSubmit={handleUpload}>
        <label className="file-input-label">
          <span className="file-input-icon">⬆️</span>
          <span>
            Click to choose files <em>(.pdf, .txt, .docx)</em>
          </span>
          <input type="file" accept=".pdf,.txt,.docx" multiple onChange={handleFileChange} />
        </label>
        {uploadedFiles.length > 0 && (
          <ul className="file-list">
            {uploadedFiles.map((file) => (
              <li key={file.name}>{file.name}</li>
            ))}
          </ul>
        )}
        <button className="btn" type="submit" disabled={uploadedFiles.length === 0}>
          Upload
        </button>
      </form>
    </div>
  );
}

export default FileUpload;
