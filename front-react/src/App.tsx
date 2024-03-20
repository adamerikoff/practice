import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Cities from './pages/Cities';
import Explore from './pages/Explore';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import Weather from './pages/Weather';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Dashboard />} />
        <Route path='/profile' element={<Profile />} />
        <Route path='/weather' element={<Weather />} />
        <Route path='/explore' element={<Explore />} />
        <Route path='/cities' element={<Cities />} />
        <Route path='/settings' element={<Settings />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
