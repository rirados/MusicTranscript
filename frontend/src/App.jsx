import { useState, useRef } from 'react';
import './index.css';

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      const selectedFile = e.target.files[0];
      if (selectedFile.name.endsWith('.wav')) {
        setFile(selectedFile);
        setError(null);
        setResults(null);
      } else {
        setError('Please select a .wav file');
        setFile(null);
      }
    }
  };

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };

  const handleSubmit = async () => {
    if (!file) return;

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/transcribe', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to transcribe audio');
      }

      const data = await response.json();
      setResults(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDownloadMidi = () => {
    if (!results || !results.midi_base64) return;
    
    const link = document.createElement('a');
    link.href = `data:audio/midi;base64,${results.midi_base64}`;
    link.download = 'transcription.mid';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="container">
      <h1>Music Transcriber</h1>
      <p className="subtitle">Upload a .wav file to extract notes and generate MIDI</p>

      <div 
        className={`upload-area ${file ? 'active' : ''}`}
        onClick={handleUploadClick}
      >
        <input 
          type="file" 
          accept=".wav" 
          ref={fileInputRef} 
          onChange={handleFileChange} 
        />
        <p>{file ? file.name : 'Click to select a .wav file'}</p>
        {!file && <span style={{ fontSize: '0.85rem', color: '#94a3b8' }}>Only .wav supported currently</span>}
      </div>

      {error && <p style={{ color: '#ef4444', marginBottom: '1rem' }}>{error}</p>}

      <button 
        className="btn" 
        onClick={handleSubmit} 
        disabled={!file || loading}
      >
        {loading ? 'Transcribing...' : 'Transcribe Audio'}
      </button>

      {loading && <div className="loading">Processing audio signal...</div>}

      {results && !loading && (
        <div className="results">
          <h2>Detected Notes ({results.notes.length})</h2>
          
          <div className="table-container">
            <table>
              <thead>
                <tr>
                  <th>Note</th>
                  <th>Freq (Hz)</th>
                  <th>Time (s)</th>
                  <th>Duration (s)</th>
                </tr>
              </thead>
              <tbody>
                {results.notes.map((note, idx) => (
                  <tr key={idx}>
                    <td>{note.note_name}</td>
                    <td>{note.frequency_hz}</td>
                    <td>{note.start_time.toFixed(2)}</td>
                    <td>{note.duration.toFixed(2)}</td>
                  </tr>
                ))}
                {results.notes.length === 0 && (
                  <tr>
                    <td colSpan="4" style={{ textAlign: 'center' }}>No notes detected.</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>

          <button className="btn success" onClick={handleDownloadMidi}>
            Download MIDI File
          </button>
        </div>
      )}
    </div>
  );
}

export default App;
