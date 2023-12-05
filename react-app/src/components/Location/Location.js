import react from 'react'
import { useSelector, useDispatch } from 'react-redux'

const Location = ({ restaurant }) => {
    const address = restaurant.address
    const open = restaurant.opening_time
    const close = restaurant.closing_time
    return (
        <>
            <h3>Location and hours</h3>
            <div>
                {address}
            </div>
            <div>
                {open} - {close}
            </div>
        </>
    )
}

export default Location;
