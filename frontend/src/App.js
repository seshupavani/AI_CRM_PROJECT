import AIAssistant from "./components/AIAssistant"
import InteractionForm from "./components/InteractionForm"
import InteractionHistory from "./components/InteractionHistory"
import VoiceRecorder from "./components/VoiceRecorder"

function App(){

return(

<div style={{padding:"30px"}}>

<h1>AI First CRM</h1>

<InteractionForm/>

<AIAssistant/>

<VoiceRecorder/>

<InteractionHistory/>

</div>

)

}

export default App