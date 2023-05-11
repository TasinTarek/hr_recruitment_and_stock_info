# my_module/controllers/main.py

from odoo import http, _
from odoo.http import request
import requests


class MyController(http.Controller):
    @http.route('/job/recruitment', type='http', auth='user', website=True)
    def my_job_route(self, **kw):
        jobs = http.request.env['hr.job'].search([])
        return http.request.render("smart_stock.recruitment_job", {
            'info': jobs,
        })


class StockController(http.Controller):

    @http.route('/stocks', type='http', auth='public', website=True)
    def get_stocks(self, **kw):
        # Replace YOUR_API_KEY with your actual API key
        # api_key = 'H7dupN8CEDZwGUyLp6Ohy_cDFOUJ4M7L'

        # Replace SYMBOLS with a comma-separated list of stock symbols to fetch
        # symbol = "GOOGL"

        # Build the API URL
        # url = f'https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/{symbol}?apiKey={api_key}'


        # Send the HTTP request
        # response = requests.get(url, headers={'X-API-Key': api_key})

        # Check if the request was successful
        # if response.status_code != 200:
            # return _('Error: Unable to fetch stock information.')

        # Parse the JSON response
        # data = response.json()

        # Extract the stock information from the response
        # stocks = []
        # for result in data['tickers']:
        #     symbol = result['ticker']
        #     price = result['lastTrade']['p']
        #     change = result['todaysChange']
        #     percent_change = result['todaysChangePerc']
        #     stocks.append({
        #         'symbol': symbol,
        #         'price': price,
        #         'change': change,
        #         'percent_change': percent_change,
        #     })

        # Render the template with the stock information
        return http.request.render('smart_stock.stock_information', {
            # 'stocks': stocks,
        })
