export {
    is_required,
    is_number,
    is_less_then,
    is_greater_then,
    validator
}


function is_required(value) {
    if (value === '') {
        return 'This field is required'
    }
    return ''
}

function is_number(value) {
    value = parseInt(value)
    if (isNaN(value)) {
        return 'is not number'
    }
    return ''
}

function is_less_then(value, args) {
    if (value < args["less_then"]){
        return `less the ${args["less_then"]}`
    }
    return ''
}

function is_greater_then(value, args) {
    if (value > args["great_then"]){
        return `more the ${args["great_then"]}`
    }
    return ''
}

function validator(value, validator_objects) {
    /**
     * @param value validation value
     * @param validator_objects [object] = {
     *     "validator_fn": "validator fun",
     *     "validator_fu_args": "args object",
     *     "is_critical": "bool",
     *     "prev_fn": "prev_fn", 
     *     "prev_fn_args": "args object",
     *     "post_fn": "post_fn", 
     *     "post_fn_args": "args object"
     * }
     * @returns object {
     *      "messages" error messages list
     *      "value" processed value
     * }
     */
    const error_messages = []
    
    for (const validator_object of validator_objects) {
        
        if (validator_object["prev_fn"]) {
            value = validator_object["prev_fn"](value, validator_object["prev_fn_args"])
        }
        
        const msg = validator_object["validator_fn"](value, validator_object["validator_fu_args"])
        if (msg !== '') {
            error_messages.push(msg)
            if (validator_object["is_critical"]) {
                break
            }
        }

        if (validator_object["post_fn"]) {
            value = validator_object["post_fn"](value, validator_object["post_fn_args"])
        }
    }

    return {
        'messages': error_messages,
        "value": value
    }
}
