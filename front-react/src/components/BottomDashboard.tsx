import BottomDashboardSideLinks from "./BottomDashboardSideLinks"
import BottomDashboardMiddle from "./BottomDashboardMiddle"
import BottomDashboardSideInfo from "./BottomDashboardSideInfo"

const BottomDashboard = () => {
  return (
    <div className='flex justify-between gap-5'>
        <BottomDashboardSideLinks/>
        <BottomDashboardMiddle/>
        <BottomDashboardSideInfo/>
    </div>
  )
}

export default BottomDashboard