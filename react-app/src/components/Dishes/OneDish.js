import { useModal } from "../../context/Modal"

const OneDish = ({ dish }) => {



    return (
        <div>
            <div>
                <h2>{dish.name}</h2>
                <span>{dish.description}</span>
            </div>
            <div>
                <h2>PIC</h2>
            </div>
            <div>
                <div>
                    ${dish.price}
                </div>
                <div>
                    quantity
                </div>
                <div>
                    add to cart
                </div>
            </div>
        </div>
    )
}


export default OneDish
