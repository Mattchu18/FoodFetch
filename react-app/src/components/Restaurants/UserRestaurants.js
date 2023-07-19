import { thunkUserRestaurants } from "../../store/restaurant";
import EditRestaurant from "./EditRestaurant";
import DeleteRestaurant from "./DeleteRestaurant";

import { thunkAllReviews } from "../../store/review";
import { useDispatch, useSelector } from "react-redux"
import { useEffect } from "react"
import { useParams } from "react-router-dom"
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import OpenModalButton from "../OpenModalButton";
import { Link } from "react-router-dom";
import "./UserRestaurants.css"


const UserRestaurants = () => {
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)


    const userRestaurantsObj = useSelector(state => state.restaurant.currentUserRestaurants)
    const userRestaurants = Object.values(userRestaurantsObj)


    useEffect(() => {
        dispatch(thunkUserRestaurants())
        // dispatch(thunkAllReviews())
    }, [dispatch])

if (user?.restaurant_owner === false || !user) return "Please log in as a Restaurant Owner to view this feature"
    // if (!userRestaurants.length) return "Please log in as a Restaurant Owner to view this feature"
    return (
        <div id="user-business-page">
            <div className="center">

                <div>
                    <h1>Manage Businesses</h1>
                </div>
                <div >
                    <Link to="/restaurants/new">Add a new Business</Link>
                </div>
                <div>
                    {userRestaurants?.length ? (<>
                        {userRestaurants.map(restaurant => (
                            <div className="business-manage-card"
                                style={{
                                    backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${restaurant?.header_image}), url("https://cdn.discordapp.com/attachments/1119886170579550301/1119886247956054026/image-coming-soon.png")`,
                                    backgroundSize: "cover",
                                    backgroundPosition: "center",
                                    color: "white",
                                    padding: "20px"
                                }}>
                                <div className="business-link">
                                    <Link to={`/restaurants/${restaurant.id}`}>
                                        <h2>{restaurant.name}</h2>
                                        <img className="business-img" src={restaurant.image}/>
                                    </Link>
                                    <div>
                                        <p>Visit your restaurant page to add entrees</p>
                                    </div>
                                </div>
                                <div className="business-details">


                                    <div className="details address">
                                        <h4>Address</h4>
                                        <p>{restaurant.address}</p>
                                    </div>
                                    <div className="details">
                                        <h4>Hours of operation</h4>
                                        <p>{restaurant.opening_time} - {restaurant.closing_time}</p>
                                    </div>
                                    <div className="details">
                                        <h4>Cuisine Type</h4>
                                        <p>{restaurant.cuisine_type}</p>
                                    </div>
                                    <div className="details">
                                        <h4>Phone number</h4>
                                        <p>{restaurant.phone_number}</p>
                                    </div>
                                    <div className="icon-container">
                                        <div className="icons">
                                            <OpenModalButton
                                                // buttonText="Edit"
                                                icon={<i class="fa-solid fa-pen-to-square"></i>}
                                                modalComponent={<EditRestaurant restaurant={restaurant} />}
                                            />

                                        </div>
                                        <div className="icons">
                                            <OpenModalButton
                                                icon={<i class="fa-solid fa-trash"></i>}
                                                modalComponent={<DeleteRestaurant restaurant={restaurant} />}
                                            />
                                            {/* delete button */}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        ))}</>
                    ) : null}
                </div>


            </div>

        </div>
    )
}

export default UserRestaurants
