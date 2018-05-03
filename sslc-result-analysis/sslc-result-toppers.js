/**
 * S.S.L.C Full A+ List
 * Copyleft Subin Siby. Licensed under GPL 3.0
 */
var ga = document.createElement('script');
ga.type = 'text/javascript';
ga.async = true;
ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'code.jquery.com/jquery-latest.js';

ga.onload = function() {
    var list = {
        10: [],
        9: [],
        8: []
    };

    $("table[align=center]").find("tr").each(function() {
        var count = 0;
        for (var i = 0; i < 10; i++) {
            if ($(this).find("td:nth-child(" + (4 + parseInt(i)) + ")").find("div[align=center]").text() != "A+") {
                count++;
            }
        }

        if (count >= 8) {
            list[count].append($(this).find("td:nth-child(3)").text());
        }
    });

    console.log(list);
};

var s = document.getElementsByTagName('script')[0];
s.parentNode.insertBefore(ga, s);
