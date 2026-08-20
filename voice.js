/**
 * Voice & Speech Engine (STT & TTS) with Lip-Sync Viseme Integration
 * Supports 11 Indian Languages.
 */

class VoiceEngine {
    constructor(onSpeechRecognized, onSpeechStarted, onSpeechEnded, avatarInstance) {
        this.onSpeechRecognized = onSpeechRecognized;
        this.onSpeechStarted = onSpeechStarted;
        this.onSpeechEnded = onSpeechEnded;
        this.avatar = avatarInstance;
        
        this.isListening = false;
        this.isSpeaking = false;
        this.recognition = null;
        this.synth = window.speechSynthesis;
        
        // Language BCP-47 mapping
        this.langMap = {
            "English": "en-IN",
            "Hindi": "hi-IN",
            "Tamil": "ta-IN",
            "Telugu": "te-IN",
            "Marathi": "mr-IN",
            "Bengali": "bn-IN",
            "Gujarati": "gu-IN",
            "Punjabi": "pa-IN",
            "Kannada": "kn-IN",
            "Malayalam": "ml-IN",
            "Urdu": "ur-IN"
        };
        
        this.currentLang = "English";
        this.initRecognition();
    }

    setLanguage(langName) {
        if (this.langMap[langName]) {
            this.currentLang = langName;
            if (this.recognition) {
                this.recognition.lang = this.langMap[langName];
            }
        }
    }

    initRecognition() {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SpeechRecognition) {
            console.warn("SpeechRecognition API not available in this browser. Fallback typing enabled.");
            return;
        }

        this.recognition = new SpeechRecognition();
        this.recognition.continuous = false;
        this.recognition.interimResults = false;
        this.recognition.lang = this.langMap[this.currentLang];

        this.recognition.onstart = () => {
            this.isListening = true;
            if (this.avatar) this.avatar.setState('listening');
            if (this.onSpeechStarted) this.onSpeechStarted();
        };

        this.recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            console.log("STT Transcript:", transcript);
            if (this.onSpeechRecognized) {
                this.onSpeechRecognized(transcript);
            }
        };

        this.recognition.onerror = (event) => {
            console.error("Speech Recognition Error:", event.error);
            this.stopListening();
        };

        this.recognition.onend = () => {
            this.isListening = false;
            if (!this.isSpeaking && this.avatar) {
                this.avatar.setState('idle');
            }
            if (this.onSpeechEnded) this.onSpeechEnded();
        };
    }

    startListening() {
        if (this.synth) this.synth.cancel(); // stop speech if listening
        if (this.recognition && !this.isListening) {
            try {
                this.recognition.lang = this.langMap[this.currentLang] || "en-IN";
                this.recognition.start();
            } catch (e) {
                console.error("Start listening failed", e);
            }
        }
    }

    stopListening() {
        if (this.recognition && this.isListening) {
            this.recognition.stop();
            this.isListening = false;
            if (this.avatar) this.avatar.setState('idle');
        }
    }

    speak(text, personaRole = 'Student', callback) {
        if (!this.synth) {
            if (callback) callback();
            return;
        }

        // Cancel existing speech
        this.synth.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = this.langMap[this.currentLang] || "en-IN";
        
        // Pitch & Rate tuning based on Persona
        if (personaRole === 'Student') {
            utterance.pitch = 1.2;
            utterance.rate = 1.0;
        } else if (personaRole === 'Parent') {
            utterance.pitch = 1.0;
            utterance.rate = 0.95;
        } else if (personaRole === 'Teacher') {
            utterance.pitch = 1.1;
            utterance.rate = 1.0;
        } else if (personaRole === 'Principal') {
            utterance.pitch = 0.85;
            utterance.rate = 0.9;
        }

        let visemeInterval = null;

        utterance.onstart = () => {
            this.isSpeaking = true;
            if (this.avatar) {
                this.avatar.setState('speaking');
            }
            
            // Viseme Lip Sync interval simulation
            visemeInterval = setInterval(() => {
                if (this.avatar && this.isSpeaking) {
                    const randomAmp = 0.2 + Math.random() * 0.7;
                    this.avatar.setViseme(randomAmp);
                }
            }, 100);
        };

        utterance.onend = () => {
            this.isSpeaking = false;
            if (visemeInterval) clearInterval(visemeInterval);
            if (this.avatar) {
                this.avatar.setState('idle');
            }
            if (callback) callback();
        };

        utterance.onerror = (e) => {
            console.error("TTS Error:", e);
            this.isSpeaking = false;
            if (visemeInterval) clearInterval(visemeInterval);
            if (this.avatar) this.avatar.setState('idle');
            if (callback) callback();
        };

        this.synth.speak(utterance);
    }
}

window.VoiceEngine = VoiceEngine;
