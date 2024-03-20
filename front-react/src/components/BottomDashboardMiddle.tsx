import heart from '../assets/heart.svg'
import pic from '../assets/pic.png'


function BottomDashboardMiddle() {
  return (
    <div className="flex flex-col gap-4 text-white">
      <div className='flex flex-col gap-3 p-6' style={{background: '#DEAB4D', borderRadius: '40px'}}>
        <div className='flex gap-1 items-center'>
          <img src={heart} alt='icon' className='h-6 w-6' />
          <h1 className='text-lg'>Activities in your area</h1>
        </div>
        <ul className="flex gap-5">
          <li>
            <img src={pic} alt='picture' className='rounded-xl'/>
            <p className='text-sm opacity-80'>500km away</p>
          </li>
          <li>
            <img src={pic} alt='picture' className='rounded-xl'/>
            <p className='text-sm opacity-80'>500km away</p>
          </li>
          <li>
            <img src={pic} alt='picture' className='rounded-xl'/>
            <p className='text-sm opacity-80'>500km away</p>
          </li>
          <li>
            <img src={pic} alt='picture' className='rounded-xl'/>
            <p className='text-sm opacity-80'>500km away</p>
          </li>
        </ul>
      </div>
      <div className='flex flex-col gap-3 p-6' style={{background: '#DEAB4D', borderRadius: '40px'}}>
        <div className='flex gap-1 items-center'>
          <img src={heart} alt='icon' className='h-6 w-6' />
          <h1 className='text-lg'>Activities in your area</h1>
        </div>
        <ul className="flex gap-5">
          <li>
            <img src={pic} alt='picture' className='rounded-xl'/>
            <p className='text-sm opacity-80'>500km away</p>
          </li>
          <li>
            <img src={pic} alt='picture' className='rounded-xl'/>
            <p className='text-sm opacity-80'>500km away</p>
          </li>
          <li>
            <img src={pic} alt='picture' className='rounded-xl'/>
            <p className='text-sm opacity-80'>500km away</p>
          </li>
          <li>
            <img src={pic} alt='picture' className='rounded-xl'/>
            <p className='text-sm opacity-80'>500km away</p>
          </li>
        </ul>
      </div>
    </div>
  )
}

export default BottomDashboardMiddle