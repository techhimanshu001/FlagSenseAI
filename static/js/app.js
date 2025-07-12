// 📦 Handle APK Upload
function uploadAPK() {
  const fileInput = document.getElementById('apkInput');
  const file = fileInput.files[0];

  if (!file || !file.name.endsWith('.apk')) {
    alert('Please upload a valid .apk file');
    return;
  }

  const formData = new FormData();
  formData.append('apk', file);

  fetch('http://localhost:5000/upload', {
    method: 'POST',
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.files && Array.isArray(data.files)) {
        alert('✅ APK uploaded and decompiled successfully!');
        loadFileList(data.files);
      } else {
        alert('⚠ Error during APK processing.');
      }
    })
    .catch((error) => {
      console.error('Upload failed:', error);
      alert('❌ Upload failed. Check if backend is running.');
    });
}

// 📃 Load Decompiled File List into UI
function loadFileList(files) {
  const fileList = document.getElementById('fileList');
  fileList.innerHTML = ''; // Clear any previous list

  files.forEach((filename) => {
    const li = document.createElement('li');
    li.textContent = filename;
    li.classList.add('clickable-file');
    li.onclick = () => fetchFileContent(filename);
    fileList.appendChild(li);
  });
}

// 📄 Fetch File Content by Filename
function fetchFileContent(filename) {
  fetch(`http://localhost:5000/file/${encodeURIComponent(filename)}`)
    .then((response) => response.text())
    .then((code) => {
      document.getElementById('fileContent').textContent = code;
    })
    .catch((error) => {
      console.error('Error loading file:', error);
      alert('❌ Could not load the file content.');
    });
}