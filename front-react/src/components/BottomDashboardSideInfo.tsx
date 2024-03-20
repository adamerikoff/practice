import icon from '../assets/icon.svg';


function BottomDashboardSideInfo() {
  return (
    <div className='flex flex-col justify-between text-sm p-4 text-white' style={{background: '#DEAB4D', borderRadius: '40px'}}>
      <div className="flex flex-col gap-3">
        <div>
          <ul className='flex gap-4 items-center'>
            <li>
              <p>SUN</p>
              <img src={icon} alt='icon' className='h-6 w-6 opacity-75' />
            </li>
            <li>
              <p>SUN</p>
              <img src={icon} alt='icon' className='h-6 w-6 opacity-75' />
            </li>
            <li>
              <p>SUN</p>
              <img src={icon} alt='icon' className='h-9 w-9' />
            </li>
            <li>
              <p>SUN</p>
              <img src={icon} alt='icon' className='h-6 w-6 opacity-75' />
            </li>
            <li>
              <p>SUN</p>
              <img src={icon} alt='icon' className='h-6 w-6 opacity-75' />
            </li>
          </ul>
        </div>
        <div className='flex items-center justify-center gap-1'>
          <img src={icon} alt='icon' className='h-4 w-4' />
          <p>8:00PM GMT</p>
        </div>
      </div>
      <ul className="flex flex-col gap-2">
        <h1>AIR CONDITIONS</h1>
        <li className="flex gap-2 items-center">
          <img src={icon} alt='icon' className='h-6 w-6' />
          <div>
            <p className='text-sm'>Rain</p>
            <p className='text-lg'>30</p>
          </div>
        </li>
        <li className="flex gap-2 items-center">
          <img src={icon} alt='icon' className='h-6 w-6' />
          <div>
            <p className='text-sm'>Wind</p>
            <p className='text-lg'>0.8 km/hr</p>
          </div>
        </li>
        <li className="flex gap-2 items-center">
          <img src={icon} alt='icon' className='h-6 w-6' />
          <div>
            <p className='text-sm'>Chance of rain</p>
            <p className='text-lg'>30 %</p>
          </div>
        </li>
        <li className="flex gap-2 items-center">
          <img src={icon} alt='icon' className='h-6 w-6' />
          <div>
            <p className='text-sm'>UV Index</p>
            <p className='text-lg'>4</p>
          </div>
        </li>
      </ul>
    </div>
  )
}

export default BottomDashboardSideInfo