// Outgoing Webhook script

// copy over from Telegram example. Update body of request sent:
// {
// 	"user": USER_NAME,
// 	"message": MESSAGE,
// 	"channel": CHANNEL_ID
// }


class Script {
    prepare_outgoing_request({ request }) {
        const webhook_token = 'SET_TOKEN';

    	let headers = {
    		'Authorization': 'Bearer ' + webhook_token
    	};

        if (request.data.bot) {
            //Don't repost messages from the bot.
            return { };
        } else {
            return {
                url: request.url,
                data: {
                    'user': request.data.user_name,
                    'message': request.data.text,
                    'channel': request.data.channel
                },
                headers: headers,
                method: 'POST'
            };
        }
    }
}
