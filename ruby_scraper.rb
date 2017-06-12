require 'HTTParty'
require 'Nokogiri'
require 'JSON'
require 'csv'

page = HTTParty.get('http://cheeseboardcollective.coop/pizza/')

parse_page = Nokogiri::HTML(page)

p parse_page.css('div').css('.pizza-list')
