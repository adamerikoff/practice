import { useState, useEffect } from 'react';

import vector from '../assets/vector.svg';
import cloud from '../assets/cloud.svg';

function TopDashboard() {
  const [city, setCity] = useState<any>(null);
  const [weather, setweather] = useState<any>(null);
  const [otherInfo, setotherInfo] = useState<any>(null);

  const apiUrl = '';

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const jsonData = await response.json();
        setCity(jsonData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  }, []);

  return (
    <header className='flex justify-between items-center'>
      {/* Left Section */}
      <div className="flex flex-col justify-between">
        {/* Top Part */}
        <div className='flex flex-col text-white'>
          <div className='flex items-center'>
            <img src={vector} alt='Vector' className='mr-2 h-8 w-8' />
            <p className='text-lg'>New York</p>
          </div>
          <div className='mt-4'><p className='text-5xl'>Cloudy</p></div>
        </div>
        
        {/* Bottom Part */}
        <div className='flex flex-col text-white mt-16'>
          <div><p className='text-9xl'>22F</p></div>
          <div><p className='text-base'>Sunday | 12 Dec 2023</p></div>
        </div>
      </div>

      {/* Right Section (Cloud SVG) */}
      <div>
        <img src={cloud} alt='Cloud' />
      </div>
    </header>
  )
}

export default TopDashboard