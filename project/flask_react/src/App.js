import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Login from './componenets/Login'
import Profile from './componenets/Profile'
import Header from './componenets/Header'
import useToken from './componenets/useToken'
import './App.css'

function App() {
    const {token, removeToken, setToken} = useToken();
    return (<BrowserRouter>
        <div className="App"><Header token={removeToken}/> {!token && token !== "" && token !== undefined ?
            <Login setToken={setToken}/> : (<> <Routes> <Route exact path="/profile" element={<Profile token={token}
                                                                                                       setToken={setToken}/>}></Route>
            </Routes> </>)} </div>
    </BrowserRouter>);
}

export default App;