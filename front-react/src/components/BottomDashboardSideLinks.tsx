import { Link } from 'react-router-dom';
import profile from '../assets/image.png';
import explore from '../assets/explore.svg';
import icon from '../assets/icon.svg';
import vector from '../assets/vector.svg';
import settings from '../assets/settings.svg';

function BottomDashboardSideLinks() {
  return (
    <div className='flex flex-col justify-between text-sm rounded-full pt-6 pb-6 pr-2 pl-2' style={{background: '#DEAB4D'}}>
      <Link to="/profile" className="text-white hover:text-gray-500 flex items-center flex-col mb-10">
        <img src={profile} alt='icon' className='h-10 w-10 rounded-full' />
        Profile
      </Link>
      <Link to="/weather" className="text-white hover:text-gray-500 flex items-center flex-col">
        <img src={icon} alt='icon' className='h-10 w-10' />
        weather
      </Link>
      <Link to="/explore" className="text-white hover:text-gray-500 flex items-center flex-col">
        <img src={explore} alt='icon' className='h-10 w-10' />
        explore
      </Link>
      <Link to="/cities" className="text-white hover:text-gray-500 flex items-center flex-col">
        <img src={vector} alt='icon' className='h-10 w-10' />
        cities
      </Link>
      <Link to="/settings" className="text-white hover:text-gray-500 flex items-center flex-col">
        <img src={settings} alt='icon' className='h-10 w-10' />
        settings
      </Link>
    </div>
  );
}

export default BottomDashboardSideLinks;
