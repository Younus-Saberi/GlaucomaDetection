import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import TipOfTheDay from './components/TipOfTheDay.jsx'
import ImageUploadComponent from './components/ImageUploadComponent.jsx'
import ImageProcessingComponent from './components/ImageProcessing.jsx'
import Navbar from './components/Navbar.jsx'
import Hero from './components/Hero.jsx'
import GoogleLoginComponent from './components/GoogleLogin.jsx'
import Analytics from './components/Analytics';
import Cards from './components/Cards';
import Newsletter from './components/Newsletter';
import Footer from './components/Footer.jsx'
import './index.css'
import { GoogleOAuthProvider } from '@react-oauth/google';
import GeminiPrompt from './components/GeminiPrompt.jsx'

const BACKENDURL = 'http://127.0.0.1:8000'

ReactDOM.createRoot(document.getElementById('root')).render(
  <GoogleOAuthProvider clientId='830534639173-5dq481qkrm457r2m6epos7g9gna1n3ou.apps.googleusercontent.com' >
    <React.StrictMode>
    <GoogleLoginComponent />
    <App backendUrl={BACKENDURL}/>
    <Hero />
    <Analytics />
    <Cards />
    <TipOfTheDay />
    <ImageUploadComponent backendUrl={BACKENDURL}/>
    <ImageProcessingComponent backendUrl={BACKENDURL}/>
    <GeminiPrompt/>
    <Newsletter />
    <Footer />
  </React.StrictMode>
  </GoogleOAuthProvider> 
)
