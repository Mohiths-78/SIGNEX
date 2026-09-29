import React from 'react'; import {createRoot} from 'react-dom/client'; import './styles.css';
function App(){return <main><h1>SIGNEX</h1><p>Bidirectional Sign Language Communication Platform</p><p>React frontend → FastAPI backend → OpenCV/MediaPipe → recognition → speech/sign avatar.</p></main>} createRoot(document.getElementById('root')).render(<App/>);
