import { useEffect } from "react"

import { useDispatch, useSelector } from "react-redux"
import { Link } from "react-router-dom"


const CuisineTypes = ({ selectedType, }) => {



    return (
        <div>

            {cuisines.map(cuisine => {(
                <div id="cuisine-types">
                    <div className="icon">
                        <i class="fa-solid fa-burger"></i>
                    </div>
                    <div className="cuisine-text">
                        <span>{cuisine}</span>
                    </div>
                </div>
            )})}
        </div>
    )

}
