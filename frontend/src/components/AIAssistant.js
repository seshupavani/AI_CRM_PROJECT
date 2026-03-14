import {useState} from "react"
import axios from "axios"

function AIAssistant(){

const[msg,setMsg]=useState("")
const[result,setResult]=useState("")

const send=async()=>{

const res=await axios.post(
"http://localhost:8000/chat",
{message:msg}
)

setResult(JSON.stringify(res.data,null,2))

}

return(

<div>

<h2>AI Assistant</h2>

<textarea
placeholder="Describe interaction"
onChange={(e)=>setMsg(e.target.value)}
style={{width:"400px",height:"100px"}}
/>

<br/>

<button onClick={send}>
Log Interaction
</button>

<pre>{result}</pre>

</div>

)

}

export default AIAssistant